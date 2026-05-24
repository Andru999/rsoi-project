import { useState, useEffect } from 'react';
import { SortFlights } from '../../enums/SortFlights';


interface useSortProps {
	sortAsc: SortFlights,
	sortDesc: SortFlights,
	sortTable: SortFlights,
	handleChangeSort: (sort: SortFlights) => void
};

export function useFlightsSort(props: useSortProps) {
	const [sort, setSort] = useState(SortFlights.IdAsc);
	const [visibility, setVisibility] = useState(false);

	const handleClicked = () => {
		if (sort === props.sortAsc) {
			setSort(props.sortDesc);
			setVisibility(true);
		}
		else if (sort === props.sortDesc) {
			setSort(SortFlights.IdAsc);
			setVisibility(false);
		}
		else {
			setSort(props.sortAsc);
			setVisibility(true);
		}
	};

	const handleMouseEnter = () => {
		setVisibility(true);
	};

	const handleMouseLeave = () => {
		if (sort !== props.sortAsc && sort !== props.sortDesc) {
			setVisibility(false);
		}
	};

	useEffect(() => {
		if (visibility || props.sortTable === props.sortDesc) {
			props.handleChangeSort(sort);
		}
	}, [sort]);

	useEffect(() => {
		if (props.sortTable !== props.sortAsc && 
				props.sortTable !== props.sortDesc && 
				props.sortTable !== SortFlights.IdAsc) {
			setSort(SortFlights.IdAsc);
			setVisibility(false);
		}
		else if (props.sortTable !== SortFlights.IdAsc) {
			setSort(props.sortTable);
			setVisibility(true);
		}
	}, [props.sortTable]);

	return { 
		sort, 
		visibility, 
		handleClicked, 
		handleMouseEnter, 
		handleMouseLeave 
	};
};
