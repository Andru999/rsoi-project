import { useState } from 'react';


export function useAuthorizationForm() {
	const [login, setLogin] = useState("");
	const [password, setPassword] = useState("");
	const [errorMsg, setErrorMsg] = useState("");
	const [invalidLogin, setInvalidLogin] = useState(false);
	const [invalidPassword, setInvalidPassword] = useState(false);

	const fieldCheck = (field: string, setInvalidField: React.Dispatch<React.SetStateAction<boolean>>) => {
		let invalidFlag = false;
		if (!field) {
			invalidFlag = true;
		}
		setInvalidField(invalidFlag);
		return !invalidFlag;
	};

	const fieldsCheck = () => {
		let resCheck = fieldCheck(login, setInvalidLogin);
		resCheck = fieldCheck(password, setInvalidPassword) && resCheck;

		return resCheck;
	};

	return { 
		login,
		password,
		errorMsg,
		invalidLogin,
		invalidPassword,
		setLogin,
		setPassword,
		setErrorMsg,
		setInvalidLogin,
		setInvalidPassword,
		fieldsCheck,
	};
};
