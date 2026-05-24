import { styled } from '@mui/material/styles';
import MuiAppBar, { AppBarProps as MuiAppBarProps } from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';

import "./Drawer.css";
import AuthService from '../../services/AuthService';
import { drawerWidth } from './MiniDrawer';
import { NavBarButton } from "../Buttons/NavBarButton";
import { AuthorizeButton } from '../Buttons/AuthorizeButton';
import { RegisterButtom } from '../Buttons/RegisterButtom';
import { IUser } from '../../interfaces/User/IUser';


interface AppBarProps extends MuiAppBarProps {
	open?: boolean;
}

const AppBar = styled(MuiAppBar, {
	shouldForwardProp: (prop) => prop !== 'open',
})<AppBarProps>(({ theme, open }) => ({
	zIndex: theme.zIndex.drawer + 1,
	transition: theme.transitions.create(['width', 'margin'], {
		easing: theme.transitions.easing.sharp,
		duration: theme.transitions.duration.leavingScreen,
	}),
	...(open && {
		marginLeft: drawerWidth,
		width: `calc(100% - ${drawerWidth}px)`,
		transition: theme.transitions.create(['width', 'margin'], {
			easing: theme.transitions.easing.sharp,
			duration: theme.transitions.duration.enteringScreen,
		}),
	}),
}));


interface DrawerNavBarProps {
	open: boolean
	user: IUser | null
	handleDrawerOpen: () => void
	handleDrawerClose: () => void
	changeUser: (user: IUser | null) => void
}

export function DrawerNavBar(props: DrawerNavBarProps) {
	return (
		<AppBar position="fixed" open={ false }>
			<Toolbar>
				<IconButton
					color="inherit"
					aria-label="open drawer"
					onClick={ props.open ? props.handleDrawerClose : props.handleDrawerOpen }
					edge="start"
				>
					<MenuIcon />
				</IconButton>

				<NavBarButton 
					text="Flight Booking System"
					link="/"
				/>

				<div className="authorization-block">
					<div className="authorization-button-container">
						{ props.user
							? 
								<AuthorizeButton 
									text="Выйти"
									link="/"
									onClick={ () => {
										AuthService.logout();
										props.changeUser(null);
									}}
								/>
							:
								<AuthorizeButton 
									text="Авторизоваться"
									link="/authorization"
								/>
						}
					</div>
					
					{ !props.user &&
						<div className="authorization-button-container">
							<RegisterButtom 
								text="Зарегистрироваться"
								link="/registration"
							/>
						</div>
					}
				</div>
			</Toolbar>
		</AppBar>
	);
}
