import { FlightsTable } from '../components/Tables/Flights/FlightsTable';
import { IUser } from '../interfaces/User/IUser';


interface FlightsPageProps {
	openMiniDrawer: boolean
	user: IUser | null
}

export function FlightsPage({ openMiniDrawer, user }: FlightsPageProps) {
	return (
		<FlightsTable 
			openMiniDrawer={ openMiniDrawer }
			user={ user }
		/>
	)
}
