import DoneIcon from '@mui/icons-material/Done';

import "./Icons.css";


interface ConfirmIconProps {
	color: string,
	addContainerClassName?: string,
	addClassName?: string,
	onClick?: () => void
}

export function ConfirmIcon(props: ConfirmIconProps) {
	return (
		<div className={ `icon-container ${props.addContainerClassName}` }>
			<div
				className={ `confirm-icon ${props.addClassName}` }
				onClick={ props.onClick }
			>
				<DoneIcon fontSize="medium" sx={{ color: props.color }}/>
			</div>
		</div>
	)
}
