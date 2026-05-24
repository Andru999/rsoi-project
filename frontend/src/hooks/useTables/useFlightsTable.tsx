import { useEffect, useState } from 'react';
import { useNavigate } from "react-router-dom";
import qs from 'qs';

import GatewayRequests from '../../requests/GatewayRequests';
import AuthService from '../../services/AuthService';
import GatewayService from '../../services/GatewayService';
import { SortFlights } from '../../enums/SortFlights';
import { IFlight } from '../../interfaces/Flight/IFlight';
import { IFilterFlight } from '../../interfaces/Flight/IFilterFlight';
import { IPrivilege } from '../../interfaces/Bonus/IPrivilege';


export function useFlightsTable() {
	let filterTableInitValue: IFilterFlight;
	let sortTableInitValue: SortFlights;
	let pageInitValue;
	let rowsPerPageInitValue;

	if (window.location.search) {
		const params = qs.parse(window.location.search.substring(1));

		filterTableInitValue = { ...params };
		pageInitValue = Number(params.page);
		rowsPerPageInitValue = Number(params.rowsPerPage);
		sortTableInitValue = (Object.values(SortFlights)).find(obj => obj === params.sortTable) ?? SortFlights.IdAsc;
	} else {
		filterTableInitValue = {};
		pageInitValue = 0;
		rowsPerPageInitValue = 20;
		sortTableInitValue = SortFlights.IdAsc;
	}

	const [flights, setFlights] = useState<IFlight[]>([]);
	const [amountFlights, setAmountFlights] = useState(0);
	const [page, setPage] = useState(pageInitValue);
	const [rowsPerPage, setRowsPerPage] = useState(rowsPerPageInitValue);
	const [sortTable, setSortTable] = useState(sortTableInitValue);
	const [filterTable, setFilterTable] = useState<IFilterFlight>(filterTableInitValue);
	const [privilege, setPrivilege] = useState<IPrivilege | null>(null);
	const [error, setError] = useState(false);
	const navigate = useNavigate();

	const handleChangePage = (
		event: React.MouseEvent<HTMLButtonElement> | null, 
		newPage: number
	) => {
		setPage(newPage);
	};

	const handleChangeRowsPerPage = (
    event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>,
  ) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

	const handleChangeSort = (value: SortFlights) => {
		setSortTable(value);
	};

	const handleChangeFilter = (value: IFilterFlight) => {
		setFilterTable(value);
		setPage(0);
	};

	const handleUpdateTable = async () => {
		await fetchFlights();
		await fetchPrivilege();
	};

	const handleUpdatePrivilege = async () => {
		await fetchPrivilege();
	};

	async function fetchFlights() {
		const response = await GatewayRequests.getListOfFlights(page, rowsPerPage, sortTable, filterTable);
		if (response) {
			setError(false);
			setFlights(response.data.items);
			setAmountFlights(response.data.totalElements);
		} else {
			setError(true);
			setFlights([]);
			setAmountFlights(0);
		}
	};

	async function fetchPrivilege() {
		if (AuthService.isAuth()) {
			const response = await GatewayService.getUserInformation();
			if (response) {
				setError(false);
				setPrivilege(response.data.privilege);
			} else {
				setError(true);
				setPrivilege(null);
			}
		};
	};

	useEffect(() => {
		const queryString = qs.stringify({
			flightNumber: filterTable.flightNumber,
			fromAirport: filterTable.fromAirport,
			toAirport: filterTable.toAirport,
			minDate: filterTable.minDate,
			maxDate: filterTable.maxDate,
			minPrice: filterTable.minPrice,
			maxPrice: filterTable.maxPrice,
			page,
			rowsPerPage,
			sortTable,
		});
		navigate(`?${queryString}`);

		fetchFlights();
	}, [page, rowsPerPage, sortTable, filterTable]);

	useEffect(() => {
		fetchPrivilege();
	}, []);

	return { 
		privilege,
		flights,
		amountFlights,
		sortTable, 
		filterTable,
		page, 
		rowsPerPage,
		error,
		handleUpdatePrivilege,
		handleUpdateTable,
		handleChangePage, 
		handleChangeRowsPerPage,
		handleChangeSort,
		handleChangeFilter,
	};
};
