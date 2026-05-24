import CreateIcon from '@mui/icons-material/Create';

import "./Icons.css";


interface ChangeIconProps {
	color: string,
	addContainerClassName?: string,
	addClassName?: string,
	onClick?: () => void
}

export function ChangeIcon(props: ChangeIconProps) {
	return (
		<div className={ `icon-container ${props.addContainerClassName}` }>
			<div
				className={ `change-icon ${props.addClassName}` }
				onClick={ props.onClick }
			>
				<CreateIcon fontSize="medium" sx={{ color: props.color }}/>
			</div>
		</div>
	)
}
