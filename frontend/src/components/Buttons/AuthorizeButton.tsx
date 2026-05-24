import { Link } from 'react-router-dom';

import "./Buttons.css";


interface AuthorizeButtonProps {
	text: string
	link: string
	onClick?: () => void
}

export function AuthorizeButton({ text, link, onClick }: AuthorizeButtonProps) {
	return (
		<Link to={ link }>
			<button 
				className="authorize-button"
				onClick={ onClick }
			>
				{ text }
			</button>
		</Link>
	)
}
