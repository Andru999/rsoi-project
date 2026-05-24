import { Route, Routes } from 'react-router-dom';

import "./App.css";
import { AuthorizationPage } from './pages/AuthorizationPage';
import { RegistrationPage } from './pages/RegistrationPage';
import { AccountPage } from './pages/AccountPage';
import { StatisticsPage } from './pages/StatisticsPage';
import { FlightsPage } from './pages/FlightsPage';
import { TicketsPage } from './pages/TicketsPage';
import { NetworkErrorPage } from './pages/NetworkErrorPage';
import { NotFoundPage } from './pages/NotFoundPage';
import { MiniDrawer } from './components/Drawer/MiniDrawer';
import { useMiniDrawer } from './hooks/useDrawers/useMiniDrawer';


function App() {
	const { 
		theme,
		open,
		user,
		handleDrawerOpen,
		handleDrawerClose,
		changeUser,
	} = useMiniDrawer();

	return (
		<div className="app-container">
			<MiniDrawer
				theme={ theme }
				open={ open }
				user={ user }
				handleDrawerOpen={ handleDrawerOpen }
				handleDrawerClose={ handleDrawerClose }
				changeUser={ changeUser }
			>
				<Routes>
					<Route 
						path="/" 
						element={ <FlightsPage openMiniDrawer={ open } user={ user }/> }
					/>
					<Route 
						path="/authorization" 
						element={ <AuthorizationPage changeUser={ changeUser }/> }
					/>
					<Route 
						path="/registration" 
						element={ <RegistrationPage changeUser={ changeUser }/> }
					/>
					{ user &&
							<Route 
								path="/tickets" 
								element={ <TicketsPage openMiniDrawer={ open } user={ user }/> }
							/>
					}
					{ user &&
							<Route
								path="/account" 
								element={ <AccountPage openMiniDrawer={ open } user={ user }/> }
							/>
					}
					{ user && user.role === "ADMIN" &&
							<Route 
								path="/statistics" 
								element={ <StatisticsPage openMiniDrawer={ open }/> }
							/>
					}
					<Route 
						path="/network_error/" 
						element={ <NetworkErrorPage openMiniDrawer={ open }/> }
					/>
					<Route 
						path="*" 
						element={ <NotFoundPage openMiniDrawer={ open }/> }
					/>
				</Routes>
			</MiniDrawer>
		</div>
	)
}

export default App;
