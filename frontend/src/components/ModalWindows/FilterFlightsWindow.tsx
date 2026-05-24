import { FilterIcon } from '../Icons/FilterIcon';

import "./ModalWindows.css";
import { Backdrop } from "./Backdrop";
import { FormButton } from "../Buttons/FormButton";
import { FormOptionallyButton } from "../Buttons/FormOptionallyButton";
import { TextHeader } from "../Texts/TextHeader";
import { InputRow } from "../Inputs/InputRow";
import { IFilterFlight } from '../../interfaces/Flight/IFilterFlight';
import { DateTimeSelection } from "../Selects/DateTimeSelection";
import { useFilterFlightsForm } from '../../hooks/useForms/useFilterFlightsForm';



interface FilterFlightsWindowProps {
	filterTable: IFilterFlight,
	onFilter: (filterFlight: IFilterFlight) => void,
	onClose: () => void
}

export function FilterFlightsWindow({ filterTable, onFilter, onClose }: FilterFlightsWindowProps) {
	const submitHandler = (event: React.FormEvent) => {
		event.preventDefault();
	};

	const keyDownHandler = (event: React.KeyboardEvent) => {
		if (event.key === "Escape") {
			onClose();
		}
	}

	const{ 
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
	} = useFilterFlightsForm({ filterTable });
	
	return (
		<>
			<Backdrop onClick={ onClose }/>

			<div className="filter-window">
				<form 
					onSubmit={ submitHandler } 
					onKeyDown={ keyDownHandler }
				>
					<TextHeader text="Поиск полетов"/>

					<div className="mb-5">
						<InputRow
							label="Номер полета"
							value={ flightNumber }
							setValue={ setFlightNumber }
						/>
					</div>

					<div className="mb-5">
						<InputRow
							label="Аэропорт отправления"
							value={ fromAirport }
							setValue={ setFromAirport }
						/>
					</div>
 
					<div className="mb-5">
						<InputRow
							label="Аэропорт прибытия"
							value={ toAirport }
							setValue={ setToAirport }
						/>
					</div>

					<div className="flex flex-row w-full mb-5 justify-center">
						<DateTimeSelection 
							label="Время вылета"
							value={ minDate }
							setValue={ setMinDate }
							addClassName="w-full"
							isInvalidRow={ invalidMinDate }
							errorText={ errorTextMinDate }
							selectHandler={ () => {
								setInvalidMinDate(false);
								if (maxDate) {
									setInvalidMaxDate(false);
								}
							}}
						/>
						<DateTimeSelection 
							label="Время прилета"
							value={ maxDate }
							setValue={ setMaxDate }
							addClassName="w-full ml-5"
							isInvalidRow={ invalidMaxDate }
							errorText={ errorTextMaxDate }
							selectHandler={ () => {
								setInvalidMaxDate(false);
								if (minDate) {
									setInvalidMinDate(false);
								}
							}}
						/>
					</div>

					<div className="flex flex-row w-full mb-5 justify-center">
						<InputRow
							label="Минимальная цена"
							value={ minPrice }
							setValue={ setMinPrice }
							isInvalidRow={ invalidMinPrice }
							helperText={ errorTextMinPrice }
							keyDownHandler={ () => setInvalidMinPrice(false) }
						/>
						<div className="w-full ml-5">
							<InputRow
								label="Максимальная цена"
								value={ maxPrice }
								setValue={ setMaxPrice }
								isInvalidRow={ invalidMaxPrice }
								helperText={ errorTextMaxPrice }
								keyDownHandler={ () => setInvalidMaxPrice(false) }
							/>
						</div>
					</div>

					<div className="left-buttons">
						<div>
							<FilterIcon
								color="gray"
								selected={ false }
								onClick={ clearFilterFields }
								addClassName="py-2 px-2 hover:bg-gray-900/10"
								addContainerClassName="basis-1/2"
							/>
						</div>
						<div className="flex flex-row justify-center w-full">
							<FormButton 
								text="Найти"
								onClick={ () => {
									if (fieldsCheck()) {
										onFilter({ 
											flightNumber, 
											fromAirport, 
											toAirport,
											minDate,
											maxDate,
											minPrice: Number(minPrice),
											maxPrice: Number(maxPrice),
										});
									}
								}}
							/>
							<FormOptionallyButton 
								text="Закрыть"
								onClick={ onClose }
							/>
						</div>
					</div>
				</form>
			</div>
		</>
	)
}
