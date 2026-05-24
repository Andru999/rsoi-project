import TextField from '@mui/material/TextField';

import { checkStringForValidity } from "./checkStringForValidity";
import { useTextInputRow } from "../../hooks/useTexts/useTextInputRow";


interface InputWithCheckRowProps {
	label: string
	value: string
	alphabet: string
	descriptionOfAcceptableCharacters: string
	setValue: (value: string) => void
	isInvalidRow?: boolean
	helperText?: string
	keyDownHandler?: () => void
}

export function InputWithCheckRow(props: InputWithCheckRowProps) {
	const changeHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
		let initialValue = event.target.value;
		let convertedValue = checkStringForValidity(initialValue, props.alphabet);
		if (convertedValue !== initialValue) {
			textInputRow.setHint(props.descriptionOfAcceptableCharacters);
		} else {
			props.setValue(convertedValue);
			textInputRow.setHint("");
		}
		
		if (props.keyDownHandler) {
			props.keyDownHandler();
		}
	}

	const textInputRow = useTextInputRow();

	return (
		<TextField
			id="outlined-required"
			value={ props.value }
			onChange={ changeHandler }
			fullWidth={ true }
			label={ props.label }
			error={ props.isInvalidRow }
			helperText={ props.isInvalidRow ? props.helperText : textInputRow.hint }
			autoComplete="off"
		/>
	)
}
