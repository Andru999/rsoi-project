import BackspaceIcon from '@mui/icons-material/Backspace';

import "./Icons.css";


interface RefundIconProps {
	color: string,
	addContainerClassName?: string,
	addClassName?: string,
	onClick?: () => void
}

export function RefundIcon(props: RefundIconProps) {
	return (
		<div className={ `icon-container ${props.addContainerClassName}` }>
			<div
				className={ `icon ${props.addClassName}` }
				onClick={ props.onClick }
			>
				<BackspaceIcon fontSize="medium" sx={{ color: props.color }}/>
			</div>
		</div>
	)
}
