import "./Texts.css";


interface TextFieldProps {
	text: string,
	addClassName?: string
}

export function TextField({ text, addClassName }: TextFieldProps) {
	return (
		<p className={ `text-field ${ addClassName }` }>
			{ text }
		</p>
	)
}
