import { useState } from 'react';


export function useBuyTicketForm() {
	const [paidFromBalance, setPaidFromBalance] = useState(false);
	
	return { 
		paidFromBalance,
		setPaidFromBalance,
	};
};
