import AccountBalanceWalletIcon from '@mui/icons-material/AccountBalanceWallet';

import "./Icons.css";


interface PayIconProps {
	color: string,
	addContainerClassName?: string,
	addClassName?: string,
	onClick?: () => void
}

export function PayIcon(props: PayIconProps) {
	return (
		<div className={ `icon-container ${props.addContainerClassName}` }>
			<div
				className={ `pay-icon ${props.addClassName}` }
				onClick={ props.onClick }
			>
				<AccountBalanceWalletIcon fontSize="medium" sx={{ color: props.color }}/>
			</div>
		</div>
	)
}
