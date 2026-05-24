import AddIconMui from '@mui/icons-material/Add';

import "./Icons.css";


interface AddIconProps {
	addContainerClassName?: string,
	addClassName?: string,
	onClick?: () => void
}

export function AddIcon(props: AddIconProps) {
	return (
		<div className={ `icon-container ${props.addContainerClassName}` }>
			<div
				className={ `add-icon ${props.addClassName}` }
				onClick={ props.onClick }
			>
				<AddIconMui fontSize="medium" sx={{ color: "white" }}/>
			</div>
		</div>
	)
}
