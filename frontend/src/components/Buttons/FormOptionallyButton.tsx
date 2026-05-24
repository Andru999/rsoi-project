import "./Buttons.css";


interface FormOptionallyButtonProps {
	text: string,
	onClick: () => void
}

export function FormOptionallyButton({ text, onClick}: FormOptionallyButtonProps) {
	return (
		<button 
			className="form-optionally-button" 
			onClick={ onClick }
		>
			{ text }
		</button>
	)
}
