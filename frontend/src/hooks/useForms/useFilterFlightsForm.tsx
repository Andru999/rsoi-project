import { useState } from 'react';

import { IFilterFlight } from '../../interfaces/Flight/IFilterFlight';


interface useFilterFlightsFormProps {
	filterTable: IFilterFlight
};

export function useFilterFlightsForm({ filterTable }: useFilterFlightsFormProps) {
	const [flightNumber, setFlightNumber] = useState(filterTable.flightNumber ?? "");
	const [fromAirport, setFromAirport] = useState(filterTable.fromAirport ?? "");
	const [toAirport, setToAirport] = useState(filterTable.toAirport ?? "");
	const [minDate, setMinDate] = useState(filterTable.minDate ?? null);
	const [maxDate, setMaxDate] = useState(filterTable.maxDate ?? null);
	const [minPrice, setMinPrice] = useState(String(filterTable.minPrice ?? ""));
	const [maxPrice, setMaxPrice] = useState(String(filterTable.maxPrice ?? ""));
	const [invalidMinDate, setInvalidMinDate] = useState(false);
	const [invalidMaxDate, setInvalidMaxDate] = useState(false);
	const [invalidMinPrice, setInvalidMinPrice] = useState(false);
	const [invalidMaxPrice, setInvalidMaxPrice] = useState(false);
	const [errorTextMinDate, setErrorTextMinDate] = useState("");
	const [errorTextMaxDate, setErrorTextMaxDate] = useState("");
	const [errorTextMinPrice, setErrorTextMinPrice] = useState("");
	const [errorTextMaxPrice, setErrorTextMaxPrice] = useState("");
	

	const fieldsCheck = () => {
		let resCheck = true;

		if (minDate && maxDate && minDate >= maxDate) {
			setInvalidMinDate(true);
			setInvalidMaxDate(true);
			setErrorTextMinDate("Время начала должно быть < времени конца");
			setErrorTextMaxDate("Время конца должно быть > времени начала");
			resCheck = false;
		}

		if (minPrice && !Number(minPrice)) {
			setInvalidMinPrice(true);
			setErrorTextMinPrice("Цена должна быть числом");
			resCheck = false;
		}

		if (maxPrice && !Number(maxPrice)) {
			setInvalidMaxPrice(true);
			setErrorTextMaxPrice("Цена должна быть числом");
			resCheck = false;
		}

		if (minPrice && maxPrice) {
			let minPriceNumber = Number(minPrice);
			let maxPriceNumber = Number(maxPrice);

			if (minPriceNumber && maxPriceNumber && minPriceNumber >= maxPriceNumber) {
				setInvalidMinPrice(true);
				setInvalidMaxPrice(true);
				setErrorTextMinPrice("Минимальная цена должна быть < максимальной");
				setErrorTextMaxPrice("Максимальная цена должна быть > минимальной");
				resCheck = false;
			}
		}

		return resCheck;
	};

	const clearFilterFields = () => {
		setFlightNumber("");
		setFromAirport("");
		setToAirport("");
		setMinDate(null);
		setMaxDate(null);
		setMinPrice("");
		setMaxPrice("");
	}

	return {
		flightNumber,
		fromAirport,
		toAirport,
		minDate,
		maxDate,
		minPrice,
		maxPrice,
		setFlightNumber,
		setFromAirport,
		setToAirport,
		setMinDate,
		setMaxDate,
		setMinPrice,
		setMaxPrice,
		invalidMinDate,
		invalidMaxDate,
		invalidMinPrice,
		invalidMaxPrice,
		errorTextMinDate,
		errorTextMaxDate,
		errorTextMinPrice,
		errorTextMaxPrice,
		setInvalidMinDate,
		setInvalidMaxDate,
		setInvalidMinPrice,
		setInvalidMaxPrice,
		clearFilterFields,
		fieldsCheck,
	};
};
