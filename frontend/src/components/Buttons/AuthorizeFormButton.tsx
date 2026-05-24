import "./Buttons.css";


interface AuthorizeFormButtonProps {
	text: string
	onClick?: () => void
}

export function AuthorizeFormButton({ text, onClick }: AuthorizeFormButtonProps) {
	return (
		<button
			type="submit" 
			className="authorize-form-button"
			onClick={ onClick }
		>
			{ text }
		</button>
	)
}
