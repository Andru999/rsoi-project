import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import GatewayService from '../../services/GatewayService';
import { ITicket } from '../../interfaces/Ticket/ITicket';


export function useTicketInfoWindow() {
	const [ticket, setTicket] = useState<ITicket>();
	const [visibility, setVisibility] = useState(false);
	const navigate = useNavigate();

	const handleOpenWindow = async (ticketUid: string) => {
		const response = await GatewayService.getInfoOnUserTicket(ticketUid);
		if (response) {
			setTicket(response.data);
			setVisibility(true);
		} else {
			navigate("/network_error");
		}
	};

	const handleCloseWindow = () => {
		setVisibility(false);
		setTicket(undefined);
	};

	return { visibility, ticket, handleOpenWindow, handleCloseWindow };
};
