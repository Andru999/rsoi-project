import "../Tables.css";
import { IFlight } from "../../../interfaces/Flight/IFlight";
import { ITicketResponse } from "../../../interfaces/Ticket/ITicketResponse";
import { PayIcon } from "../../Icons/PayIcon";
import { IUser } from '../../../interfaces/User/IUser';
import { IPrivilege } from "../../../interfaces/Bonus/IPrivilege";
import { BuyTicketWindow } from "../../ModalWindows/BuyTicketWindow";
import { useWindow } from "../../../hooks/useWindows/useWindow";


interface FlightsRowProps {
	flight: IFlight
	user: IUser | null
	privilege: IPrivilege | null
	handleOpenPurchaseInfoWindow: (ticket: ITicketResponse) => void
	handleUpdatePrivilege: () => Promise<void>
	addClassName?: string
}

export function FlightsRow(props: FlightsRowProps) {
	const buyTicketWindow = useWindow();

	return (
		<>
			<div
				className={ `row ${ props.addClassName }` }
				onDoubleClick={ props.user ? buyTicketWindow.handleOpenWindow : undefined }
			>
				<div className="row-item basis-1/6">{ props.flight.flightNumber }</div>
				<div className="row-item basis-1/4">{ props.flight.fromAirport }</div>
				<div className="row-item basis-1/4">{ props.flight.toAirport }</div>
				<div className="row-item basis-1/5">{ props.flight.date }</div>
				<div className="row-item basis-1/6">{ props.flight.price }</div>
				
				<div className="actions">
					{ props.user && 
						<PayIcon 
							color="gray"
							addClassName="px-2 py-2"
							onClick={ buyTicketWindow.handleOpenWindow }
						/>
					}
				</div>
			</div>

			{ buyTicketWindow.visibility &&
				<BuyTicketWindow
					flight={ props.flight }
					privilege={ props.privilege }
					onClose={ buyTicketWindow.handleCloseWindow }
					handleOpenPurchaseInfoWindow={ props.handleOpenPurchaseInfoWindow }
					handleUpdatePrivilege={ props.handleUpdatePrivilege }
				/>
			}
		</>
	)
}
