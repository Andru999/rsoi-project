import { useEffect, useState } from 'react';

import GatewayService from '../../services/GatewayService';
import { IPrivilegeResponse } from '../../interfaces/Bonus/IPrivilegeResponse';


export function usePrivilegeInfo() {
	const [privilegeInfo, setPrivilegeInfo] = useState<IPrivilegeResponse>();
	const [error, setError] = useState(false);

	async function handleUpdatePrivilegeInfo() {
		await fetchPrivilegeInfo();
	};

	const addZero = (value: number) => {
		if (value < 10) {
			return "0" + value;
		} else {
			return "" + value;
		}
	};

	const selectDate = (dateString: string, addYaer=true) => {
		let date = new Date(dateString);
		let resDate = `${addZero(date.getMonth() + 1)}-${addZero(date.getDate())}`
		return addYaer ? `${date.getFullYear()}-${resDate}`: resDate;
	};

	const selectTime = (dateString: string) => {
		let date = new Date(dateString);
		return `${date.getHours()}:${addZero(date.getMinutes())}:${addZero(date.getSeconds())}`;
	};

	async function fetchPrivilegeInfo() {
		const response = await GatewayService.getInfoAboutBonusAccount();
		if (response) {
			setError(false);
			setPrivilegeInfo(response.data);
		} else {
			setError(true);
		}
	};

	useEffect(() => {
		fetchPrivilegeInfo();
	}, []);

	return { 
		privilegeInfo,
		error,
		handleUpdatePrivilegeInfo,
		selectDate,
		selectTime,
	};
};
