import "./Account.css";
import { IUser } from "../../interfaces/User/IUser";
import { TextRow } from "../Texts/TextRow";


interface UserInfoProps {
	user: IUser
}

export function UserInfo({ user }: UserInfoProps) {
	return (
		<div className="user-info-body">
			<TextRow 
				label="Логин"
				text={ user.login }
			/>
			<TextRow 
				label="Имя"
				text={ user.firstname }
			/>
			<TextRow 
				label="Фамилия"
				text={ user.lastname }
			/>
			<TextRow 
				label="Роль"
				text={ user.role }
			/>
			<TextRow 
				label="Почта"
				text={ user.email }
			/>
			<TextRow 
				label="Телефон"
				text={ user.phone }
			/>
		</div>
	)
}
