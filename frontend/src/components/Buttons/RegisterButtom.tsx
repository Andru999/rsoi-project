import { Link } from 'react-router-dom';

import "./Buttons.css";


interface RegisterButtomProps {
	text: string
	link: string
	onClick?: () => void
}

export function RegisterButtom({ text, link, onClick}: RegisterButtomProps) {
	return (
		<Link to={ link }>
			<button 
				className="register-button" 
				onClick={ onClick }
			>
				{ text }
			</button>
		</Link>
	)
}
