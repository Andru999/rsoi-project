import "./Page.css";
import { Account } from "../components/Account/Account";
import { IUser } from '../interfaces/User/IUser';


interface AccountPageProps {
	openMiniDrawer: boolean
	user: IUser
}

export function AccountPage({ openMiniDrawer, user }: AccountPageProps) {
	return (
		<div className={`${openMiniDrawer ? "short-page-container" : "long-page-container"}`}>
			<Account 
				user={ user }
			/>
		</div>
	)
}
