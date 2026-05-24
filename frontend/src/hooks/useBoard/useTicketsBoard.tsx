import { useEffect, useState } from 'react';

import GatewayService from '../../services/GatewayService';
import { IUserInfo } from '../../interfaces/User/IUserInfo';


export function useTicketsBoard() {
	const [userInfo, setUserInfo] = useState<IUserInfo>();
	const [error, setError] = useState(false);

	async function handleUpdateTable() {
		await fetchUserInfo();
	};

	async function ticketRefund(ticketUid: string) {
		const response = await GatewayService.ticketRefund(ticketUid)
		if (response?.status === 204) {
			await fetchUserInfo();
		} else {
			setError(true);
		}
	};

	async function fetchUserInfo() {
		const response = await GatewayService.getUserInformation();
		if (response) {
			setError(false);
			setUserInfo(response.data);
		} else {
			setError(true);
			setUserInfo(undefined);
		}
	};
	
	useEffect(() => {
		fetchUserInfo();
	}, []);

	return { 
		userInfo,
		error,
		handleUpdateTable,
		ticketRefund,
	};
};
