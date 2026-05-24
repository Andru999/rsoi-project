import { useState } from 'react';

import { IFilterFlight } from '../../interfaces/Flight/IFilterFlight';


interface useFilterFlightsWindowProps {
	handleChangeFilter: (filterTable: IFilterFlight) => void
};

export function useFilterFlightsWindow({ handleChangeFilter }: useFilterFlightsWindowProps) {
	const [visibility, setVisibility] = useState(false);

	const handleOpenWindow = () => {
		setVisibility(true);
	};

	const handleCloseWindow = () => {
		setVisibility(false);
	};

	const handleSearch = (filterFlight: IFilterFlight) => {
		handleChangeFilter({
			flightNumber: filterFlight.flightNumber || undefined,
			fromAirport: filterFlight.fromAirport || undefined,
			toAirport: filterFlight.toAirport || undefined,
			minDate: filterFlight.minDate || undefined,
			maxDate: filterFlight.maxDate || undefined,
			minPrice: filterFlight.minPrice || undefined,
			maxPrice: filterFlight.maxPrice || undefined,
		});
		handleCloseWindow();
	};

	return { visibility, handleOpenWindow, handleCloseWindow, handleSearch };
};
