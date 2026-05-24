import "./Texts.css";


interface TextHeaderProps {
	text: string,
	addClassName?: string
}

export function TextHeader({ text, addClassName }: TextHeaderProps) {
	return (
		<p className={ `text-header ${ addClassName }` }>
			{ text }
		</p>
	)
}
