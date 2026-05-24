import { useState } from 'react';


export function useRegistrationForm() {
	const [login, setLogin] = useState("");
	const [password, setPassword] = useState("");
	const [firstname, setFirstname] = useState("");
	const [lastname, setLastname] = useState("");
	const [email, setEmail]  = useState("");
	const [phone, setPhone] = useState("");
	const [errorMsg, setErrorMsg] = useState("");
	const [invalidLogin, setInvalidLogin] = useState(false);
	const [invalidPassword, setInvalidPassword] = useState(false);
	const [invalidFirstname, setInvalidFirstname] = useState(false);
	const [invalidLastname, setInvalidLastname] = useState(false);
	const [invalidEmail, setInvalidEmail] = useState(false);
	const [invalidPhone, setInvalidPhone] = useState(false);

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
		resCheck = fieldCheck(firstname, setInvalidFirstname) && resCheck;
		resCheck = fieldCheck(lastname, setInvalidLastname) && resCheck;
		resCheck = fieldCheck(email, setInvalidEmail) && resCheck;
		resCheck = fieldCheck(phone, setInvalidPhone) && resCheck;

		return resCheck;
	};

	return { 
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
	};
};
