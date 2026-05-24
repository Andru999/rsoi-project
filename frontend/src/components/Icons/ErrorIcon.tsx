import ErrorOutlineIcon from '@mui/icons-material/ErrorOutline';

import "./Icons.css";


interface ErrorIconProps {
	color: string,
	addContainerClassName?: string,
	addClassName?: string,
	onClick?: () => void
}

export function ErrorIcon(props: ErrorIconProps) {
	return (
		<div className={ `icon-container ${props.addContainerClassName}` }>
			<div
				className={ `icon ${props.addClassName}` }
				onClick={ props.onClick }
			>
				<ErrorOutlineIcon fontSize="medium" sx={{ color: props.color }}/>
			</div>
		</div>
	)
}