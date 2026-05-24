import { Link } from 'react-router-dom';

import "./Buttons.css";


interface NavBarButtonProps {
	text: string
	link: string
}

export function NavBarButton({ text, link }: NavBarButtonProps) {
	return (
		<Link to={ link }>
			<button className="navbar-button">
				{ text }
			</button>
		</Link>
	)
}
