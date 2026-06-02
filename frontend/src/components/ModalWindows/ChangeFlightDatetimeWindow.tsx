import dayjs, { Dayjs } from "dayjs";
import { useState } from "react";

import "./ModalWindows.css";
import { IFlight } from "../../interfaces/Flight/IFlight";
import GatewayService from "../../services/GatewayService";
import { Backdrop } from "./Backdrop";
import { DateTimeSelection } from "../Selects/DateTimeSelection";
import { FormButton } from "../Buttons/FormButton";
import { TextField } from "../Texts/TextField";
import { TextHeader } from "../Texts/TextHeader";
import { TextRow } from "../Texts/TextRow";


interface ChangeFlightDatetimeWindowProps {
	flight: IFlight
	onClose: () => void
	onUpdated: () => Promise<void>
}

export function ChangeFlightDatetimeWindow(props: ChangeFlightDatetimeWindowProps) {
	const [datetime, setDatetime] = useState<Dayjs | null>(dayjs(props.flight.date));
	const [errorText, setErrorText] = useState("");

	const handleConfirm = async () => {
		if (!datetime) {
			setErrorText("Укажите новое время вылета");
			return;
		}

		if (!datetime.isAfter(dayjs())) {
			setErrorText("Время вылета должно быть в будущем");
			return;
		}

		const response = await GatewayService.updateFlightDatetime(
			props.flight.flightNumber,
			datetime.toISOString(),
		);

		if (!response) {
			setErrorText("Не удалось перенести рейс. Проверьте время вылета и права доступа");
			return;
		}

		await props.onUpdated();
		props.onClose();
	};

	return (
		<>
			<Backdrop onClick={ props.onClose }/>

			<div className="add-window">
				<TextHeader text="Перенос времени вылета"/>

				<div className="window-body">
					<TextRow label="Рейс" text={ props.flight.flightNumber }/>
					<TextRow label="Текущее время" text={ props.flight.date }/>
					<DateTimeSelection
						label="Новое время вылета"
						value={ datetime }
						setValue={ setDatetime }
						isInvalidRow={ Boolean(errorText) }
						errorText={ errorText }
					/>
					{ errorText && <TextField text={ errorText } addClassName="text-red-600"/> }
				</div>

				<div className="right-buttons">
					<FormButton text="Сохранить" onClick={ handleConfirm }/>
					<FormButton text="Отмена" onClick={ props.onClose }/>
				</div>
			</div>
		</>
	);
}
