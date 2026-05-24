import { Authorization } from "../components/Auth/Authorization"
import { IUser } from "../interfaces/User/IUser"


interface AuthorizationPageProps {
	changeUser: (user: IUser | null) => void
}

export function AuthorizationPage({ changeUser }: AuthorizationPageProps) {
	return (
		<Authorization
			changeUser={ changeUser }
		/>
	)
}
