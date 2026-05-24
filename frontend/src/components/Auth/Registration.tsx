import Alert from '@mui/material/Alert';
import { useNavigate } from "react-router-dom";

import "../ModalWindows/ModalWindows.css";
import AuthService from '../../services/AuthService';
import UserService from '../../services/UserService';
import { TextHeader } from "../Texts/TextHeader";
import { InputRow } from "../Inputs/InputRow";
import { useRegistrationForm } from '../../hooks/useForms/useRegistrationForm';
import { AuthorizeFormButton } from '../Buttons/AuthorizeFormButton';
import { IUser } from '../../interfaces/User/IUser';


interface RegistrationProps {
	changeUser: (user: IUser | null) => void
}

export function Registration({ changeUser }: RegistrationProps) {
	const submitHandler = (event: React.FormEvent) => {
		event.preventDefault();
	};

	const keyDownHandler = async (event: React.KeyboardEvent) => {
		if (event.key === "Escape") {
			await register();
		}
	}

	const register = async () => {
    if (fieldsCheck()) {
			const response = await AuthService.register({
        login, password, email, phone, lastname, firstname
      });
      if (response) {
        setErrorMsg(response);
      } else {
				changeUser(await UserService.getMe());
        navigate("/");
      }
    }
  };

	const navigate = useNavigate();

	const { 
		login,
		password,
		firstname,
		lastname,
		email,
		phone,
		errorMsg,
		invalidLogin,
		invalidPassword,
		invalidFirstname,
		invalidLastname,
		invalidEmail,
		invalidPhone,
		setLogin,
		setPassword,
		setFirstname,
		setLastname,
		setEmail,
		setPhone,
		setErrorMsg,
		setInvalidLogin,
		setInvalidPassword,
		setInvalidFirstname,
		setInvalidLastname,
		setInvalidEmail,
		setInvalidPhone,
		fieldsCheck,
	} = useRegistrationForm()

	return (
		<>
			<div className="authorization-window">
				<form 
					onSubmit={ submitHandler } 
					onKeyDown={ keyDownHandler }
				>
					<TextHeader text="Регистрация"/>
					
					<div className="mb-5">
						<InputRow
							label="Логин*"
							value={ login }
							setValue={ setLogin }
							isInvalidRow={ invalidLogin }
							helperText="Обязательное поле"
							keyDownHandler={ () => setInvalidLogin(false) }
						/>
					</div>

					<div className="mb-5">
						<InputRow
							label="Пароль*"
							value={ password }
							setValue={ setPassword }
							type="password"
							isInvalidRow={ invalidPassword }
							helperText="Обязательное поле"
							keyDownHandler={ () => setInvalidPassword(false) }
						/>
					</div>

					<div className="mb-5">
						<InputRow
							label="Фамилия*"
							value={ lastname }
							setValue={ setLastname }
							isInvalidRow={ invalidLastname }
							helperText="Обязательное поле"
							keyDownHandler={ () => setInvalidLastname(false) }
						/>
					</div>

					<div className="mb-5">
						<InputRow
							label="Имя*"
							value={ firstname }
							setValue={ setFirstname }
							isInvalidRow={ invalidFirstname }
							helperText="Обязательное поле"
							keyDownHandler={ () => setInvalidFirstname(false) }
						/>
					</div>

					<div className="mb-5">
						<InputRow
							label="Почта*"
							value={ email }
							setValue={ setEmail }
							isInvalidRow={ invalidEmail }
							helperText="Обязательное поле"
							keyDownHandler={ () => setInvalidEmail(false) }
						/>
					</div>

					<InputRow
						label="Телефон*"
						value={ phone }
						setValue={ setPhone }
						isInvalidRow={ invalidPhone }
						helperText="Обязательное поле"
						keyDownHandler={ () => setInvalidPhone(false) }
					/>

					{ errorMsg &&
						<Alert
							sx={{fontWeight: 1000}}
							severity="error"
							className="mt-5"
						>
							{ errorMsg }
						</Alert>
					}

					<div className="h-11 mt-5 flex flex-col justify-center">
						<AuthorizeFormButton 
							text="Зарегистрироваться"
							onClick={ register }
						/>
					</div>
				</form>
			</div>
		</>
	)
}
