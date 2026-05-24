import ClearIcon from '@mui/icons-material/Clear';

import "./Icons.css";


interface RejectIconProps {
	color: string,
	addContainerClassName?: string,
	addClassName?: string,
	onClick?: () => void
}

export function RejectIcon(props: RejectIconProps) {
	return (
		<div className={ `icon-container ${props.addContainerClassName}` }>
			<div
				className={ `reject-icon ${props.addClassName}` }
				onClick={ props.onClick }
			>
				<ClearIcon fontSize="medium" sx={{ color: props.color }}/>
			</div>
		</div>
	)
}
