import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ExpandLess from '@material-ui/icons/ExpandLess';
import ExpandMore from '@material-ui/icons/ExpandMore';


interface DrawerDropdownListProps {
	openDrawer: boolean
	openList: boolean
	text: string
	handleClick: () => void
	icon?: React.ReactNode
	children?: React.ReactNode
}

export function DrawerDropdownList(props: DrawerDropdownListProps) {
	return (
		<>
			<ListItem 
				disablePadding
				sx={{ display: 'block' }}
				key={ props.text }
				onClick={ props.handleClick }
			>
				<ListItemButton
					sx={{
						minHeight: 48,
						justifyContent: props.openDrawer ? 'initial' : 'center',
						px: 2.5,
					}}
				>
					<ListItemIcon
						sx={{
							minWidth: 0,
							mr: props.openDrawer ? 3 : 'auto',
							justifyContent: 'center',
						}}
					>
						{ props.icon }
					</ListItemIcon>

					<ListItemText 
						primary={
							<p className='text-xl text-gray-600'>
								{ props.text }
							</p>
						}
						sx={{ opacity: props.openDrawer ? 1 : 0 }} 
					/>

					{ props.openDrawer && 
						( props.openList 
							? <ExpandLess style={{ color: "#374151" }}/>
							: <ExpandMore style={{ color: "#374151" }}/>
						)
					}
				</ListItemButton>
			</ListItem>
			{ props.children }
		</>
	)
}
