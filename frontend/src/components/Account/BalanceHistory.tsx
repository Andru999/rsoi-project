import "./Account.css";
import { TextField } from '../Texts/TextField';
import { TextSubtitle } from '../Texts/TextSubtitle';
import { TicketIcon } from '../Icons/TicketIcon';
import { IPrivilegeHistory } from '../../interfaces/Bonus/IPrivilegeHistory';
import { TicketInfoWindow } from "../ModalWindows/TicketInfoWindow";
import { useTicketInfoWindow } from "../../hooks/useWindows/useTicketInfoWindow";
import { ITicket } from "../../interfaces/Ticket/ITicket";


interface BalanceHistoryProps {
	history: IPrivilegeHistory[]
	selectDate: (dateString: string, addYaer?: boolean) => string
	selectTime: (dateString: string) => string
}

export function BalanceHistory({ history, selectDate, selectTime }: BalanceHistoryProps) {
	const ticketInfoWindow = useTicketInfoWindow()

	return (
		<>
			<div className="detailed-info-body">
				{ history.map((balanceHistory) => 
						<div 
							className="my-2"
							key={ balanceHistory.ticketUid }
						>
							<div className="flex flex-row mt-2">
								<div 
									className="balance-history-info"
									onDoubleClick={ async () => { 
										await ticketInfoWindow.handleOpenWindow(balanceHistory.ticketUid);
									}}
								>
									<TextField 
										text={ balanceHistory.operationType ==="FILL_IN_BALANCE" 
										? "Дата и время покупки билета:" 
										: "Дата и время сдачи билета:" 
									}
									/>
									<div className="flex flex-row">
										<TextSubtitle
											text={ selectDate(balanceHistory.date) }
										/>
										<TextField
											text={ selectTime(balanceHistory.date) }
											addClassName="ml-4"
										/>
									</div>

									<TextField 
										text={ balanceHistory.operationType ==="FILL_IN_BALANCE" 
											? "Начислено бонусов:" 
											: "Списано бонусов:" 
										}
									/>
									<div className={ balanceHistory.operationType ==="FILL_IN_BALANCE" 
											? "accrued-bonuses" 
											: "reducted-bonuses" 
										}
									>
										{ `${balanceHistory.balanceDiff}` }
									</div>
								</div>

								<div className="flex flex-row justify-center ml-1 mr-0">
									<TicketIcon 
										color="gray"
										addClassName="px-2 py-2 hover:bg-gray-900/10"
										onClick={ async () => { 
											await ticketInfoWindow.handleOpenWindow(balanceHistory.ticketUid);
										}}
									/>
								</div>
							</div>
						</div>
					)
				}
			</div>

			{ ticketInfoWindow.visibility &&
				<TicketInfoWindow
					ticket={ ticketInfoWindow.ticket as ITicket}
					onClose={ ticketInfoWindow.handleCloseWindow }
				/>
			}
		</>
	)
}
