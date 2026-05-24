import { useEffect, useState } from 'react';
import { useTheme } from '@mui/material/styles';

import AuthService from '../../services/AuthService';
import UserService from '../../services/UserService';
import { IUser } from '../../interfaces/User/IUser';


export function useMiniDrawer() {
	const theme = useTheme();
	const [open, setOpen] = useState(false);
	const [user, setUser] = useState<IUser | null>(null);

	const handleDrawerOpen = () => {
		setOpen(true);
	};

	const handleDrawerClose = () => {
		setOpen(false);
	};

	const changeUser = (user: IUser | null) => {
		setUser(user);
	};

	const fetchCurrentUser = async () => {
		if (AuthService.isAuth()) {
			setUser(await UserService.getMe());
		}
	};

	useEffect(() => {
		fetchCurrentUser();
	}, []);

	return { 
		theme,
		open,
		user,
		handleDrawerOpen,
		handleDrawerClose,
		changeUser,
	};
};
