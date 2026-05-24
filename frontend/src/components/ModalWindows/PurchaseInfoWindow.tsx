import Alert from '@mui/material/Alert';

import "./ModalWindows.css";
import { Backdrop } from "./Backdrop";
import { FormButton } from "../Buttons/FormButton";
import { TextHeader } from "../Texts/TextHeader";
import { ITicketResponse } from "../../interfaces/Ticket/ITicketResponse";


interface PurchaseInfoWindowProps {
	ticket: ITicketResponse
	onClose: () => void
}

export function PurchaseInfoWindow({ ticket, onClose }: PurchaseInfoWindowProps) {
	return (
		<>
			<Backdrop onClick={ onClose }/>

			<div className="info-window">
				<TextHeader text={ "Информация по билету" }/>

				<Alert
					sx={{ fontSize: 18 }}
					severity="success"
				>
					{`Вы купили билет на рейс номер ${ticket.flightNumber} по направлению ${ticket.fromAirport} - ${ticket.toAirport}, вылет запланирован на ${ticket.date}. Вам доступно ${ticket.privilege.balance} бонусов. Благодарим за покупку!`}
				</Alert>

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
