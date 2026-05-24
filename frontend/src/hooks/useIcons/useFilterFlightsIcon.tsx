import { useState, useEffect } from 'react';

import { IFilterFlight } from '../../interfaces/Flight/IFilterFlight';


interface useFilterFlightsIconProps {
	filterTable: IFilterFlight
};

export function useFilterFlightsIcon({ filterTable }: useFilterFlightsIconProps) {
	const checkFilterTable = () => {
		return filterTable.flightNumber ||
			filterTable.fromAirport ||
			filterTable.toAirport ||
			filterTable.minDate ||
			filterTable.maxDate ||
			filterTable.minPrice ||
			filterTable.maxPrice
	}
	
	const [active, setActive] = useState(checkFilterTable() ? true : false);

	useEffect(() => {
		if (checkFilterTable()) {
			setActive(true);
		} else {
			setActive(false);
		}
	}, [filterTable]);

	return { active };
};
