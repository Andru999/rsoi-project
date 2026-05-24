import AirplaneTicketIcon from '@mui/icons-material/AirplaneTicket';

import "./Icons.css";


interface TicketIconProps {
	color: string,
	addContainerClassName?: string,
	addClassName?: string,
	onClick?: () => void
}

export function TicketIcon(props: TicketIconProps) {
	return (
		<div className={ `icon-container ${props.addContainerClassName}` }>
			<div
				className={ `icon ${props.addClassName}` }
				onClick={ props.onClick }
			>
				<AirplaneTicketIcon fontSize="medium" sx={{ color: props.color }}/>
			</div>
		</div>
	)
}
