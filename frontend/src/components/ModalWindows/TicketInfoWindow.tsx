import "./ModalWindows.css";
import { Backdrop } from "./Backdrop";
import { FormButton } from "../Buttons/FormButton";
import { TextHeader } from "../Texts/TextHeader";
import { TextRow } from '../Texts/TextRow';
import { ITicket } from '../../interfaces/Ticket/ITicket';


interface TicketInfoWindowProps {
	ticket: ITicket
	onClose: () => void
}

export function TicketInfoWindow({ ticket, onClose }: TicketInfoWindowProps) {
	
	return (
		<>
			<Backdrop onClick={ onClose }/>

			<div className="info-window">
				<TextHeader text={ "Информация по билету" }/>

				<div className="mb-5">
					<TextRow
						label="Номер рейса"
						text={ ticket.flightNumber }
					/>
				</div>

				<div className="mb-5">
					<TextRow
						label="Аэропорт отправления"
						text={ ticket.fromAirport }
					/>
				</div>

				<div className="mb-5">
					<TextRow
						label="Аэропорт прибытия"
						text={ ticket.toAirport }
					/>
				</div>

				<div className="mb-5">
					<TextRow
						label="Дата и время вылета"
						text={ ticket.date }
					/>
				</div>

				<div className="mb-5">
					<TextRow
						label="Цена билета"
						text={ `${ticket.price}` }
					/>
				</div>

				<div className="right-buttons">
					<FormButton 
						text="Ок"
						onClick={ onClose }
					/>
				</div>
			</div>
		</>
	)
}
