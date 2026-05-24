import Alert from '@mui/material/Alert';
import Switch from '@mui/material/Switch';
import { useNavigate } from "react-router-dom";

import "./ModalWindows.css";
import GatewayService from '../../services/GatewayService';
import { Backdrop } from "./Backdrop";
import { FormButton } from "../Buttons/FormButton";
import { FormOptionallyButton } from "../Buttons/FormOptionallyButton";
import { TextHeader } from "../Texts/TextHeader";
import { TextField } from "../Texts/TextField";
import { TextRow } from '../Texts/TextRow';
import { ConfirmationWindow } from "./ConfirmationWindow";
import { ITicketResponse } from '../../interfaces/Ticket/ITicketResponse';
import { IPrivilege } from '../../interfaces/Bonus/IPrivilege';
import { IFlight } from '../../interfaces/Flight/IFlight';
import { useBuyTicketForm } from "../../hooks/useForms/useBuyTicketForm";
import { useWindow } from "../../hooks/useWindows/useWindow";


interface BuyTicketWindowProps {
	flight: IFlight
	privilege: IPrivilege | null
	onClose: () => void
	handleOpenPurchaseInfoWindow: (ticket: ITicketResponse) => void
	handleUpdatePrivilege: () => Promise<void>
}

export function BuyTicketWindow(props: BuyTicketWindowProps) {
	const submitHandler = (event: React.FormEvent) => {
		event.preventDefault();
	};

	const keyDownHandler = (event: React.KeyboardEvent) => {
		if (event.key === "Escape") {
			props.onClose();
		}
	};

	const { 
		paidFromBalance,
		setPaidFromBalance,
	} = useBuyTicketForm();

	const confirmBuyWindow = useWindow();
	const navigate = useNavigate();
	
	return (
		<>
			<Backdrop onClick={ props.onClose }/>

			<div className="add-window">
				<form 
					onSubmit={ submitHandler } 
					onKeyDown={ keyDownHandler }
				>
					<TextHeader text="Покупка билета"/>

					<Alert
						sx={{	fontSize: 18 }}
						severity="info"
					>
						{`Вам доступно ${props.privilege?.balance} бонусов`}
					</Alert>

					<div className="m-5 flex flex-row justify-center items-center">
						<TextField
							text="Воспользоваться бонусами для оплаты билета"
							addClassName="w-full"
						/>
						<Switch 
							checked={ paidFromBalance }
							onChange={ () => setPaidFromBalance(!paidFromBalance) }
						/>
					</div>

					<div className="central-buttons">
						<FormButton 
							text="Купить"
							onClick={ confirmBuyWindow.handleOpenWindow }
						/>
						<FormOptionallyButton 
							text="Закрыть"
							onClick={ props.onClose }
						/>
					</div>
				</form>
			</div>

			{ confirmBuyWindow.visibility && 
				<ConfirmationWindow 
					header="Подтвердите закрытие окна"
					onClose={ props.onClose }
					onConfirm={ () => {
							confirmBuyWindow.handleCloseWindow();
							props.onClose();
						}
					}
				/>
			}

			{ confirmBuyWindow.visibility && 
				<ConfirmationWindow 
					header="Подтвердите покупку билета"
					children={
						<>
							<div className="mb-5">
								<TextRow
									label="Номер рейса"
									text={ props.flight.flightNumber }
								/>
							</div>
							<div className="mb-5">
								<TextRow
									label="Аэропорт отправления"
									text={ props.flight.fromAirport }
								/>
							</div>
							<div className="mb-5">
								<TextRow
									label="Аэропорт прибытия"
									text={ props.flight.toAirport }
								/>
							</div>
							<div className="mb-5">
								<TextRow
									label="Дата и время отправления"
									text={ props.flight.date }
								/>
							</div>
							<TextRow
								label="Цена"
								text={ `${props.flight.price}` }
							/>
						</>
					}
					onClose={ confirmBuyWindow.handleCloseWindow }
					onConfirm={ async () => {
							const response = await GatewayService.buyTicket(
								{ 
									flightNumber: props.flight.flightNumber,
									price: props.flight.price,
									paidFromBalance,
								}
							);
							if (response) {
								confirmBuyWindow.handleCloseWindow();
								props.onClose();
								props.handleOpenPurchaseInfoWindow(response.data);
								await props.handleUpdatePrivilege();
							} else {
								navigate("/network_error");
							}
						}
					}
				/>
			}
		</>
	)
}
