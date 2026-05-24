import "./Buttons.css";


interface FormButtonProps {
	text: string,
	onClick?: () => void
}

export function FormButton({ text, onClick }: FormButtonProps) {
	return (
		<button 
			type="submit" 
			className="form-button" 
			onClick={ onClick }
		>
			{ text }
		</button>
	)
}
