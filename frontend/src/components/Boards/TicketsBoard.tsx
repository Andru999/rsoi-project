import Alert from '@mui/material/Alert';

import "./Boards.css";
import { TicketsItem } from "./TicketsItem";
import { DataLoadError } from "../DataLoadError/DataLoadError";
import { IUser } from '../../interfaces/User/IUser';
import { useTicketsBoard } from "../../hooks/useBoard/useTicketsBoard";


interface TicketsBoardProps {
	openMiniDrawer: boolean
	user: IUser
}

export function TicketsBoard({ openMiniDrawer, user }: TicketsBoardProps) {
	const { 
		userInfo,
		error,
		handleUpdateTable,
		ticketRefund,
	} = useTicketsBoard();

	return (
		<>
			<div className={`${openMiniDrawer ? "short-board-container" : "long-board-container"}`}>
				{ userInfo &&
					<Alert
						sx={{	fontSize: 18 }}
						severity="info"
					>
						{`${user.firstname}, на Вашем счету ${userInfo.privilege.balance} бонусов`}
					</Alert>
				}
				<div className="board">
					{ !error
						?	<div className="tickets-list">
								{ userInfo?.tickets.map(ticket => 
										<TicketsItem 
											ticket={ ticket }
											ticketRefund={ ticketRefund }
											key={ ticket.ticketUid } 
										/>
									)
								}
							</div>
						: <DataLoadError 
								handleUpdate={ handleUpdateTable }
							/>
					}
				</div>
			</div>
		</>
	)
}
