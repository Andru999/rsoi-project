import { useEffect, useState } from 'react';
import { useNavigate } from "react-router-dom";
import qs from 'qs';

import StatisticsService from '../../services/StatisticsService';
import { IStatistics } from '../../interfaces/Statistics/IStatistics';


interface StatusCodeCounter {
  x200: number
  x300: number
  x400: number
  x500: number
}

interface MethodCounter {
  GET: number
  HEAD: number
  POST: number
  PUT: number
	DELETE: number
	CONNECT: number
	OPTIONS: number
	TRACE: number
	PATCH: number
}

function countStatusCode(items: IStatistics[]): StatusCodeCounter {
  const counter: StatusCodeCounter = {
    x200: 0,
    x300: 0,
    x400: 0,
    x500: 0,
  }

  for (const item of items) {
    if (item.status_code >= 200 && item.status_code < 300) {
      counter.x200 += 1;
    } else if (item.status_code >= 300 && item.status_code < 400) {
      counter.x300 += 1;
    } else if (item.status_code >= 400 && item.status_code < 500) {
      counter.x400 += 1;
    } else if (item.status_code >= 500 && item.status_code < 600) {
      counter.x500 += 1;
    }
  }

  return counter;
}

function countMethod(items: IStatistics[]): MethodCounter {
  const counter: MethodCounter = {
    GET: 0,
		HEAD: 0,
		POST: 0,
		PUT: 0,
		DELETE: 0,
		CONNECT: 0,
		OPTIONS: 0,
		TRACE: 0,
		PATCH: 0,
  }

  for (const item of items) {
    if (item.method === "GET") {
      counter.GET += 1;
    } else if (item.method === "HEAD") {
      counter.HEAD += 1;
    } else if (item.method === "POST") {
      counter.POST += 1;
    } else if (item.method === "PUT") {
      counter.PUT += 1;
    } else if (item.method === "DELETE") {
      counter.DELETE += 1;
    } else if (item.method === "CONNECT") {
      counter.CONNECT += 1;
    } else if (item.method === "OPTIONS") {
      counter.OPTIONS += 1;
    } else if (item.method === "TRACE") {
      counter.TRACE += 1;
    } else if (item.method === "PATCH") {
      counter.PATCH += 1;
    }
  }

  return counter;
}

export function useStatisticsTable() {
	let pageInitValue;
	let rowsPerPageInitValue;

	if (window.location.search) {
		const params = qs.parse(window.location.search.substring(1));
		pageInitValue = Number(params.page);
		rowsPerPageInitValue = Number(params.rowsPerPage);
	} else {
		pageInitValue = 0;
		rowsPerPageInitValue = 20;
	}

	const [statistics, setStatistics] = useState<IStatistics[]>([]);
	const [statusCodeChart, setStatusCodeChart] = useState<StatusCodeCounter>();
	const [methodChart, setMethodChart] = useState<MethodCounter>();
	const [amountStatistics, setAmountStatistics] = useState(0);
	const [page, setPage] = useState(pageInitValue);
	const [rowsPerPage, setRowsPerPage] = useState(rowsPerPageInitValue);
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

	const handleUpdateTable = async () => {
		await fetchStatistics();
	};

	async function fetchStatistics() {
		const response = await StatisticsService.getAll(page, rowsPerPage);
		if (response) {
			setError(false);
			setStatistics(response.data.items);
			setStatusCodeChart(countStatusCode(response.data.items));
			setMethodChart(countMethod(response.data.items));
			setAmountStatistics(response.data.totalElements);
		} else {
			setError(true);
			setStatistics([]);
			setStatusCodeChart(undefined);
			setMethodChart(undefined);
			setAmountStatistics(0);
		}
	};

	useEffect(() => {
		const queryString = qs.stringify({
			page,
			rowsPerPage,
		});
		navigate(`?${queryString}`);

		fetchStatistics();
	}, [page, rowsPerPage]);

	return { 
		statistics,
		statusCodeChart,
		methodChart,
		amountStatistics,
		page, 
		rowsPerPage,
		error,
		handleUpdateTable,
		handleChangePage, 
		handleChangeRowsPerPage,
	};
};
