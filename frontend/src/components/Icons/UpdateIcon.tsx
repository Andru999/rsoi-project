import RefreshIcon from '@mui/icons-material/Refresh';

import "./Icons.css";


interface UpdateIconProps {
	color: string,
	addContainerClassName?: string,
	addClassName?: string,
	onClick?: () => void
}

export function UpdateIcon(props: UpdateIconProps) {
	return (
		<div className={ `icon-container ${props.addContainerClassName}` }>
			<div
				className={ `icon ${props.addClassName}` }
				onClick={ props.onClick }
			>
				<RefreshIcon fontSize="medium" sx={{ color: props.color }}/>
			</div>
		</div>
	)
}
