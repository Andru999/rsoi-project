import "./Texts.css";


interface TextSubtitleProps {
	text: string,
	addClassName?: string
}

export function TextSubtitle({ text, addClassName }: TextSubtitleProps) {
	return (
		<p className={ `text-subtitle ${ addClassName }` }>
			{ text }
		</p>
	)
}
