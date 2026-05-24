import TextField from '@mui/material/TextField';


interface TextRowProps {
	label: string
	text: string
}

export function TextRow(props: TextRowProps) {
	return (
		<TextField
			id="outlined-required"
			value={ props.text }
			fullWidth={ true }
			label={ props.label }
			InputProps={{
				readOnly: true,
			}}
		/>
	)
}
