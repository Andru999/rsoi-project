import { useState } from 'react';

import { ITicketResponse } from '../../interfaces/Ticket/ITicketResponse';


export function usePurchaseInfoWindow() {
	const [ticket, setTicket] = useState<ITicketResponse>();
	const [visibility, setVisibility] = useState(false);

	const handleOpenWindow = (ticket: ITicketResponse) => {
		setTicket(ticket);
		setVisibility(true);
	};

	const handleCloseWindow = () => {
		setVisibility(false);
	};

	return { visibility, ticket, handleOpenWindow, handleCloseWindow };
};
