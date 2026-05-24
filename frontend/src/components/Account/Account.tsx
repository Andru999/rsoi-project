import Alert from '@mui/material/Alert';

import "./Account.css";
import { DataLoadError } from '../DataLoadError/DataLoadError';
import { TextHeader } from '../Texts/TextHeader';
import { BalanceHistory } from './BalanceHistory';
import { UserInfo } from './UserInfo';
import { IUser } from '../../interfaces/User/IUser';
import { usePrivilegeInfo } from '../../hooks/useAccount/usePrivilegeInfo';


interface AccountProps {
	user: IUser
}

export function Account({ user }: AccountProps) {
	const {
		privilegeInfo,
		error,
		handleUpdatePrivilegeInfo,
		selectDate,
		selectTime,
	} = usePrivilegeInfo();

	return (
		<>
			{ !error
				?	<>
						{ privilegeInfo &&
							<div className="detailed-info-container">
								<TextHeader
									text="Информация о пользователе и история покупок билетов"
								/>

								<UserInfo
									user={ user }
								/>

								<div className="my-5">
									<Alert
										sx={{ fontSize: 18 }}
										severity="info"
									>
										{`На Вашем счету ${privilegeInfo.balance} бонусов`}
									</Alert>
								</div>

								<BalanceHistory 
									history={ privilegeInfo.history }
									selectDate={ selectDate }
									selectTime={ selectTime }
								/>
							</div>
						}
					</>
				: <DataLoadError 
						handleUpdate={ handleUpdatePrivilegeInfo }
					/>
			}
		</>
	)
}
