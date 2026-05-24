import "../Tables.css";
import { FlightsTitleRow } from "./FlightsTitleRow";
import { FlightsRow } from "./FlightsRow";
import { TablePagination } from '../TablePagination';
import { DataLoadError } from "../../DataLoadError/DataLoadError";
import { FilterFlightsWindow } from "../../ModalWindows/FilterFlightsWindow";
import { PurchaseInfoWindow } from "../../ModalWindows/PurchaseInfoWindow";
import { ITicketResponse } from "../../../interfaces/Ticket/ITicketResponse";
import { IUser } from '../../../interfaces/User/IUser';
import { usePurchaseInfoWindow } from "../../../hooks/useWindows/usePurchaseInfoWindow";
import { useFlightsTable } from "../../../hooks/useTables/useFlightsTable";
import { useFilterFlightsWindow } from "../../../hooks/useWindows/useFilterFlightsWindow";


interface FlightsTableProps {
	openMiniDrawer: boolean
	user: IUser | null
}

export function FlightsTable({ openMiniDrawer, user }: FlightsTableProps) {
	const { 
		privilege,
		flights,
		amountFlights,
		sortTable, 
		filterTable,
		page, 
		rowsPerPage,
		error,
		handleUpdatePrivilege,
		handleUpdateTable,
		handleChangePage, 
		handleChangeRowsPerPage,
		handleChangeSort,
		handleChangeFilter,
	} = useFlightsTable();

	const filterFlightsWindow = useFilterFlightsWindow({ handleChangeFilter });
	const purchaseInfoWindow = usePurchaseInfoWindow();

	return (
		<>
			<div className={`${openMiniDrawer ? "short-table-container" : "long-table-container"}`}>
				<div className="table">
					<FlightsTitleRow 
						sortTable={ sortTable }
						filterTable={ filterTable }
						handleChangeSort={ handleChangeSort }
						handleOpenFilterWindow={ filterFlightsWindow.handleOpenWindow }
					/>

					<div className="rows-container">
						{ !error
							?	<div className="rows">
									{ flights.map((flight, index) => 
											<FlightsRow 
												key={ flight.flightNumber }
												flight={ flight } 
												user={ user }
												privilege={ privilege }
												handleOpenPurchaseInfoWindow={ purchaseInfoWindow.handleOpenWindow }
												handleUpdatePrivilege={ handleUpdatePrivilege }
												addClassName={index % 2 ? "bg-gray-200": "bg-white"}
											/>
										)
									}
								</div>
							: <DataLoadError 
									handleUpdate={ handleUpdateTable }
								/>
						}
					</div>

					<TablePagination
						amountItems={ amountFlights }
						page={ page }
						handleChangePage={ handleChangePage }
						rowsPerPage={ rowsPerPage }
						handleChangeRowsPerPage={ handleChangeRowsPerPage }
					/>
				</div>
			</div>

			{ filterFlightsWindow.visibility && 
				<FilterFlightsWindow 
					filterTable={ filterTable }
					onFilter={ filterFlightsWindow.handleSearch } 
					onClose={ filterFlightsWindow.handleCloseWindow }
				/> 
			}

			{ purchaseInfoWindow.visibility && 
				<PurchaseInfoWindow 
					ticket={ purchaseInfoWindow.ticket as ITicketResponse }
					onClose={ purchaseInfoWindow.handleCloseWindow }
				/>
			}
		</>
	)
}
