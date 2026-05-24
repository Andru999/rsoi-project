import { Registration } from "../components/Auth/Registration"
import { IUser } from "../interfaces/User/IUser"


interface RegistrationPageProps {
	changeUser: (user: IUser | null) => void
}

export function RegistrationPage({ changeUser }: RegistrationPageProps) {
	return (
		<Registration
			changeUser={ changeUser }
		/>
	)
}
