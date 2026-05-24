import TextField from '@mui/material/TextField';


interface InputRowProps {
	label: string
	value: string
	setValue: (value: string) => void
	type?: string
	isInvalidRow?: boolean
	disabled?: boolean
	helperText?: string
	keyDownHandler?: () => void
}

export function InputRow(props: InputRowProps) {
	const changeHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
		props.setValue(event.target.value);
		
		if (props.keyDownHandler) {
			props.keyDownHandler();
		}
	}

	return (
		<TextField
			id="outlined-required"
			value={ props.value }
			onChange={ changeHandler }
			fullWidth={ true }
			label={ props.label }
			type={ props.type }
			error={ props.isInvalidRow }
			disabled={ props.disabled }
			helperText={ props.isInvalidRow ? props.helperText : "" }
			autoComplete="off"
		/>
	)
}
